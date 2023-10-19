'use client'
import Button from '@/components/Button'
import Input from '@/components/Input'
import { useRouter } from 'next/navigation'
import { FormEvent, useState } from 'react'

export default function Home() {
  const router = useRouter()
  const [state, setState] = useState({
    column: 0,
    row: 0,
  })

  function handleChange(inputName: 'column' | 'row', value: string) {
    setState((prev) => ({ ...prev, [inputName]: value }))
  }

  function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault()

    const { row, column } = state

    if (row >= 1 && column >= 2) {
      router.push(`/program/?row=${row}&column=${column}`)
    }
  }

  return (
    <main className="flex flex-col items-center space-y-8">
      <div className="flex w-full justify-center space-x-2 border-b border-gray-300 bg-gradient-to-b from-zinc-200 pb-6 pt-8 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit lg:w-auto  lg:rounded-xl lg:border lg:bg-gray-200 lg:p-4 lg:dark:bg-zinc-800/30">
        <p>Estrutura de dados não linear</p>
        <p>-</p>
        <p className="font-bold">Atividade A*</p>
      </div>

      <form
        onSubmit={handleSubmit}
        className="flex flex-col space-y-4 sm:w-full md:w-1/2 xl:w-1/2"
      >
        <h3 className="text-center text-2xl">Informe o tamanho do tabuleiro</h3>

        <label className="flex flex-col" htmlFor="row">
          Linhas:
          <Input
            id="row"
            name="row"
            type="number"
            min={1}
            value={state.row}
            required
            placeholder="Digite o número de linhas..."
            onChange={(e) => handleChange('row', e.target.value)}
          />
        </label>

        <label className="flex flex-col" htmlFor="column">
          Colunas:
          <Input
            id="column"
            name="column"
            type="number"
            min={2}
            value={state.column}
            required
            placeholder="Digite o número de colunas..."
            onChange={(e) => handleChange('column', e.target.value)}
          />
        </label>

        <Button>Enviar</Button>
      </form>
    </main>
  )
}
