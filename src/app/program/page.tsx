'use client'
import Button from '@/components/Button'
import Cell from '@/components/Cell'
import { CellTypes } from '@/types/cell'
import { useSearchParams } from 'next/navigation'
import { useEffect, useState } from 'react'
import { aStarSearch } from './AStar'

export default function Program() {
  const searchParams = useSearchParams()
  const [config, setConfig] = useState({
    sourceWasChosen: false,
    targetWasChosen: false,
    sourceIndexs: { row: 0, column: 0 },
    targetIndex: { row: 0, column: 0 },
  })
  const [grid, setGrid] = useState<CellTypes[][]>([])

  useEffect(() => {
    const rowSize = parseInt(searchParams.get('row') || '0')
    const columnSize = parseInt(searchParams.get('column') || '0')

    const initialState: CellTypes[][] = new Array(rowSize)

    for (let i = 0; i < rowSize; i++) {
      initialState[i] = new Array<CellTypes>(columnSize)
      for (let j = 0; j < columnSize; j++) {
        initialState[i][j] = {
          isBlocked: false,
          isTarget: false,
          isSource: false,
          wasVisited: false,
          parent_row: -1,
          parent_column: -1,
          h: -1,
          g: -1,
          f: -1,
        }
      }
    }

    setGrid(initialState)
  }, [searchParams])

  function changeCellStatus(
    rowNumber: number,
    columnNumber: number,
    status: 'isSource' | 'isTarget' | 'isBlocked',
    statusValue = true,
  ) {
    switch (status) {
      case 'isBlocked':
        if (
          !grid[rowNumber][columnNumber].isSource ||
          !grid[rowNumber][columnNumber].isTarget
        ) {
          setGrid((prev) => {
            const newGrid = [...prev]

            newGrid[rowNumber][columnNumber] = {
              ...prev[rowNumber][columnNumber],
              [status]: statusValue,
            }
            return newGrid
          })
        }
        break
      case 'isTarget':
        if (!grid[rowNumber][columnNumber].isSource) {
          setGrid((prev) => {
            const newGrid = [...prev]

            newGrid[rowNumber][columnNumber] = {
              ...prev[rowNumber][columnNumber],
              [status]: statusValue,
            }
            return newGrid
          })
          setConfig((prev) => ({
            ...prev,
            targetWasChosen: true,
            targetIndex: { row: rowNumber, column: columnNumber },
          }))
        }
        break
      default:
        setGrid((prev) => {
          const newGrid = [...prev]

          newGrid[rowNumber][columnNumber] = {
            ...prev[rowNumber][columnNumber],
            [status]: statusValue,
          }
          return newGrid
        })
        setConfig((prev) => ({
          ...prev,
          sourceWasChosen: true,
          sourceIndex: { row: rowNumber, column: columnNumber },
        }))
        break
    }
  }

  return (
    <main className="flex flex-col items-center space-y-8">
      <div className="flex w-full justify-center space-x-2 border-b border-gray-300 bg-gradient-to-b from-zinc-200 pb-6 pt-8 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit lg:w-auto  lg:rounded-xl lg:border lg:bg-gray-200 lg:p-4 lg:dark:bg-zinc-800/30">
        <p>Estrutura de dados não linear</p>
        <p>-</p>
        <p className="font-bold">Atividade A*</p>
      </div>

      <section>
        {grid.map((array, i) => {
          return (
            <div key={i} className="flex">
              {array.map((item, j) => (
                <Cell
                  key={`${i}${j}`}
                  data={{ ...item, id: parseInt(`${i}${j}`) }}
                  onClick={() => {
                    changeCellStatus(
                      i,
                      j,
                      !config.sourceWasChosen
                        ? 'isSource'
                        : !config.targetWasChosen
                        ? 'isTarget'
                        : 'isBlocked',
                      !item.isBlocked,
                    )
                  }}
                  // onMouseLeave={() => {
                  //   if (config.targetWasChosen) {
                  //     changeCellStatus(i, j, 'isBlocked', !item.isBlocked)
                  //   }
                  // }}
                />
              ))}
            </div>
          )
        })}
      </section>

      <Button
        onClick={() =>
          aStarSearch([...grid], config.sourceIndexs, config.targetIndex)
        }
      >
        Iniciar
      </Button>
    </main>
  )
}
