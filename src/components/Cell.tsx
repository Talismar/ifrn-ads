import React, { ComponentProps } from 'react'
import { CellTypes } from '@/types/cell'

interface CellProps extends ComponentProps<'div'> {
  data: CellTypes & { id: number }
}

function Cell({ data, ...rest }: CellProps) {
  return (
    <div
      className={`flex h-24 w-24 flex-col justify-between border-[1px] border-blue-500 
      ${
        data.isSource
          ? 'bg-green-600'
          : data.isTarget
          ? 'bg-red-600'
          : data.isBlocked
          ? 'bg-gray-600'
          : data.wasVisited
          ? 'bg-blue-200'
          : 'bg-slate-50'
      } 
       px-2 py-1 `}
      {...rest}
    >
      <div className="flex justify-between font-mono text-sm text-black">
        <span>{data.f}</span>
        <span>{data.id}</span>
      </div>
      <div className="flex justify-between font-mono text-sm text-black">
        <span>{data.g}</span>
        <span>{data.h}</span>
      </div>
    </div>
  )
}

export default Cell
