import React, { ComponentProps } from 'react'

type SelectProps = ComponentProps<'select'>

function Select({ ...rest }: SelectProps) {
  return <select className="rounded-md p-2 text-black" {...rest} />
}

export default Select
