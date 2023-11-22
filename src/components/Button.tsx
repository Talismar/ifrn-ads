import React, { ComponentProps } from 'react'

interface ButtonProps extends ComponentProps<'button'> {
  children: string
  variant?: 'primary' | 'secondary'
}

function Button({ variant = 'primary', children, ...rest }: ButtonProps) {
  const variantClasses = variant === 'primary' ? 'bg-blue-500' : 'bg-orange-500'

  return (
    <button className={`rounded-md ${variantClasses} p-2 font-bold`} {...rest}>
      {children}
    </button>
  )
}

export default Button
