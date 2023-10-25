import React, { ComponentProps } from 'react'

type InputProps = ComponentProps<'input'>

function Input({ ...rest }: InputProps) {
  return <input type="text" className="rounded-md p-2 text-black" {...rest} />
}

export default Input
