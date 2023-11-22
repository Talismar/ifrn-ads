import Image from "next/image";
import React, { ComponentProps } from "react";

interface CellProps extends ComponentProps<"div"> {
  data: {
    id: number;
    row: number;
    column: number;
    isSource: boolean;
    isTarget: boolean;
    isBlocked: boolean;
    isPath: boolean;
    g: number;
    h: number;
    f: number;
  };
}

function Cell({ data, ...rest }: CellProps) {
  const cellColor = data.isSource
    ? "border-green-900 bg-green-500"
    : data.isTarget
      ? "border-red-900 bg-red-500"
      : data.isBlocked
        ? "border-gray-900 bg-gray-500"
        : data.isPath
          ? "border-blue-900 bg-blue-500"
          : data.g !== 0
            ? "border-pink-900 bg-pink-500"
            : "border-slate-900 bg-slate-50";

  return (
    <div
      className={`relative flex h-24 w-24 flex-col justify-between border-[1px] ${cellColor} px-2 py-1 `}
      {...rest}
    >
      {/* {data.isSource ? (
        <Image
          src="/Screenshot from 2023-11-22 14-49-27.png"
          alt="Gato"
          layout="fill"
          objectFit="cover"
        />
      ) : data.isTarget ? (
        <Image
          src="/r7lg_f6vb_210528.jpg"
          alt="Rato"
          layout="fill"
          objectFit="cover"
        />
      ) : ( */}
      <>
        <div className="flex justify-between font-mono text-sm text-black">
          <span>{Math.ceil(data.f)}</span>
          <span>{data.id}</span>
        </div>
        <div className="flex justify-between font-mono text-sm text-black">
          <span>{data.g}</span>
          <span>{Math.ceil(data.h)}</span>
        </div>
      </>
      {/* )} */}
    </div>
  );
}

export default Cell;
