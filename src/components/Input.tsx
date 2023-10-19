import React, { ComponentProps } from 'react';

interface InputProps extends ComponentProps<"input"> {

}

function Input({...rest}: InputProps) {
  return (
    <input type="text" className='text-black p-2 rounded-md' {...rest} />
  );
}

export default Input;