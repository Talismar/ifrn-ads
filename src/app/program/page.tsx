'use client'
import Button from '@/components/Button'
import Cell from '@/components/Cell'
import useAStarSearch from '@/hooks/useAStarSearch'
import { useSearchParams } from 'next/navigation'
import { useEffect } from 'react'

export default function Program() {
  const searchParams = useSearchParams()
  const {
    run,
    setConfig,
    handleChangeCellStatus,
    gridState,
    wasFound,
    processFinished,
  } = useAStarSearch()

  useEffect(() => {
    const rowSize = parseInt(searchParams.get('row') || '0')
    const columnSize = parseInt(searchParams.get('column') || '0')
    const algoritm = searchParams.get('algoritm')

    if (algoritm === 'manhattanDistance' || algoritm === 'euclideanDistance') {
      setConfig((prev) => ({
        ...prev,
        size: { row: rowSize, column: columnSize },
        algoritm,
      }))
    }
  }, [searchParams])

  return (
    <main className="flex flex-col items-center space-y-8 p-4">
      <div className="flex w-full justify-center space-x-2 border-b border-gray-300 bg-gradient-to-b from-zinc-200 pb-6 pt-8 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit lg:w-auto  lg:rounded-xl lg:border lg:bg-gray-200 lg:p-4 lg:dark:bg-zinc-800/30">
        <p>Estrutura de dados não linear</p>
        <p>-</p>
        <p className="font-bold">Atividade A*</p>
      </div>

      {processFinished && (
        <h1>
          {wasFound ? 'Caminho encontrado' : 'Não existe um caminho até o alvo'}
        </h1>
      )}

      <section>
        {gridState.map((array, i) => {
          return (
            <div key={i} className="flex">
              {array.map((item, j) => (
                <Cell
                  key={`${i}${j}`}
                  data={{
                    ...item,
                    id: parseInt(`${i}${j}`),
                  }}
                  onClick={() => {
                    handleChangeCellStatus(i, j, !item.isBlocked)
                  }}
                />
              ))}
            </div>
          )
        })}
      </section>

      <div className="flex space-x-4">
        <Button
          onClick={() => {
            run()
          }}
        >
          Iniciar
        </Button>
        <Button
          onClick={() => {
            window.location.reload()
          }}
          variant="secondary"
        >
          Resetar
        </Button>
      </div>
    </main>
  )
}
