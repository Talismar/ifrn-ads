import React, { ComponentProps } from 'react'

interface ButtonProps extends ComponentProps<'button'> {
  children: string
}

function Button({ children, ...rest }: ButtonProps) {
  return (
    <button className="rounded-md bg-blue-500 p-2 font-bold" {...rest}>
      {children}
    </button>
  )
}

export default Button
