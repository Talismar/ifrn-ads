/* eslint-disable no-use-before-define */
import { useEffect, useState } from 'react'

class Cell {
  row: number
  column: number
  isSource: boolean
  isTarget: boolean
  isBlocked: boolean
  isPath: boolean
  g: number
  h: number
  f: number
  parent: any

  constructor(
    row: number,
    column: number,
    isSource: boolean,
    isTarget: boolean,
    isBlocked: boolean,
  ) {
    this.row = row
    this.column = column
    this.isSource = isSource
    this.isTarget = isTarget
    this.isBlocked = isBlocked
    this.isPath = false

    this.g = 0 // distância da célula inicial até esta
    this.h = 0 // heurística - estimativa da distância até o destino
    this.f = 0 // custo total: F = G + H
    this.parent = null
  }

  manhattanDistance(target: Cell) {
    return (
      Math.abs(this.row - target.row) + Math.abs(this.column - target.column)
    )
  }

  euclideanDistance(target: Cell) {
    const dx = this.row - target.row
    const dy = this.column - target.column
    return Math.sqrt(dx * dx + dy * dy)
  }
}

function AStar(
  grid: Cell[][],
  source: Cell,
  target: Cell,
  algoritm: 'manhattanDistance' | 'euclideanDistance',
) {
  const openSet = [source]
  const closedSet = new Set()

  while (openSet.length > 0) {
    let current = openSet[0]

    // Buscar o no que tenha o menor custo para explorar
    for (let i = 1; i < openSet.length; i++) {
      if (openSet[i].f < current.f) {
        current = openSet[i]
      }
    }

    openSet.splice(openSet.indexOf(current), 1)
    closedSet.add(current)

    if (current === target) {
      const path = []
      let temp = current
      while (temp) {
        path.push(temp)
        temp = temp.parent
        if (temp !== null && temp !== source) {
          temp.isPath = true
        }
      }

      const wasFound = true
      return [path.reverse(), closedSet, wasFound]
    }

    const { row, column } = current

    const successors = [
      { newRow: row - 1, newColumn: column, cost: 10 }, // left
      { newRow: row + 1, newColumn: column, cost: 10 }, // right
      { newRow: row, newColumn: column - 1, cost: 10 }, // top
      { newRow: row, newColumn: column + 1, cost: 10 }, // bottom
      { newRow: row - 1, newColumn: column - 1, cost: 14 }, // left | top
      { newRow: row - 1, newColumn: column + 1, cost: 14 }, // left | bottom
      { newRow: row + 1, newColumn: column - 1, cost: 14 }, // right | top
      { newRow: row + 1, newColumn: column + 1, cost: 14 }, // right | bottom
    ]

    for (const { newRow, newColumn, cost } of successors) {
      if (
        newRow >= 0 &&
        newRow < grid.length &&
        newColumn >= 0 &&
        newColumn < grid[0].length
      ) {
        const neighbor = grid[newRow][newColumn]
        if (!neighbor.isBlocked && !closedSet.has(neighbor)) {
          const tempG = current.g + cost

          if (!openSet.includes(neighbor) || tempG < neighbor.g) {
            neighbor.g = tempG
            neighbor.h = neighbor[algoritm](target) // Ou use calculateEuclideanDistance para distância euclidiana
            neighbor.f = neighbor.g + neighbor.h
            neighbor.parent = current

            if (!openSet.includes(neighbor)) {
              openSet.push(neighbor)
            }
          }
        }
      }
    }
  }

  const wasFound = false
  return [null, null, wasFound]
}

type IndexTypes = { row: number; column: number }
type ConfigTypes = {
  sourceWasChosen: boolean
  targetWasChosen: boolean
  wasFound: boolean
  processFinished: boolean
  sourceIndex: IndexTypes
  targetIndex: IndexTypes
  size: IndexTypes
  algoritm: 'manhattanDistance' | 'euclideanDistance'
}

export default function useAStarSearch() {
  const [gridState, setGridState] = useState<Cell[][]>([])
  const [config, setConfig] = useState<ConfigTypes>({
    sourceWasChosen: false,
    targetWasChosen: false,
    wasFound: false,
    processFinished: false,
    sourceIndex: { row: 0, column: 0 },
    targetIndex: { row: 0, column: 0 },
    size: { row: 0, column: 0 },
    algoritm: 'manhattanDistance',
  })

  useEffect(() => {
    if (config.size.row && config.size.column && !config.sourceWasChosen) {
      setGridState(
        new Array(config.size.row)
          .fill(null)
          .map((_, row) =>
            new Array(config.size.column)
              .fill(null)
              .map((_, column) => new Cell(row, column, false, false, false)),
          ),
      )
    }
  }, [config])

  function handleChangeCellStatus(
    rowNumber: number,
    columnNumber: number,
    statusValue = true,
  ) {
    const { sourceWasChosen, targetWasChosen } = config

    if (!sourceWasChosen) {
      setGridState((prev) => {
        const newGrid = [...prev]

        newGrid[rowNumber][columnNumber].isSource = true
        newGrid[rowNumber][columnNumber].f = 0
        newGrid[rowNumber][columnNumber].g = 0
        newGrid[rowNumber][columnNumber].h = 0

        return newGrid
      })
      setConfig((prev) => ({
        ...prev,
        sourceWasChosen: true,
        sourceIndex: { row: rowNumber, column: columnNumber },
      }))
    }

    //
    else if (!targetWasChosen && !gridState[rowNumber][columnNumber].isSource) {
      setGridState((prev) => {
        const newGrid = [...prev]

        newGrid[rowNumber][columnNumber].isTarget = true

        return newGrid
      })
      setConfig((prev) => ({
        ...prev,
        targetWasChosen: true,
        targetIndex: { row: rowNumber, column: columnNumber },
      }))
    }

    //
    else {
      if (
        !gridState[rowNumber][columnNumber].isSource ||
        !gridState[rowNumber][columnNumber].isTarget
      ) {
        setGridState((prev) => {
          const newGrid = [...prev]

          newGrid[rowNumber][columnNumber].isBlocked = statusValue
          return newGrid
        })
      }
    }
  }

  function run() {
    const grid = [...gridState]
    // console.log(config.sourceIndex, config.targetIndex)

    const sourceCell = grid[config.sourceIndex.row][config.sourceIndex.column]
    const targetCell = grid[config.targetIndex.row][config.targetIndex.column]

    const [path, closedSet, wasFound] = AStar(
      grid,
      sourceCell,
      targetCell,
      config.algoritm,
    )

    if (wasFound) {
      // console.log(closedSet)

      console.log('Caminho encontrado:', path)
      setGridState([...grid])
    } else {
      setGridState([...grid])
      console.log('Caminho não encontrado')
    }

    if (typeof wasFound === 'boolean') {
      setConfig((prev) => ({
        ...prev,
        wasFound,
        processFinished: true,
      }))
    }
  }

  return {
    gridState,
    setConfig,
    run,
    handleChangeCellStatus,
    wasFound: config.wasFound,
    processFinished: config.processFinished,
  }
}
