/* eslint-disable no-use-before-define */
import { ConfigTypes } from "@/types";
import Cell from "@/utils/cell";
import { print_out } from "@/utils/print_out";
import { useEffect, useState } from "react";

class AStar {
  grid: Cell[][] = [];

  constructor(grid: Cell[][]) {
    this.grid = grid;
  }

  getGridItemByType(type: "predador" | "presa") {
    for (let i = 0; i < this.grid.length; i++) {
      for (let j = 0; j < this.grid[0].length; j++) {
        const element = this.grid[i][j];
        if (
          (type === "predador" && element.isSource) ||
          (type === "presa" && element.isTarget)
        ) {
          return element;
        }
      }
    }
  }

  clearGrid() {
    for (let i = 0; i < this.grid.length; i++) {
      for (let j = 0; j < this.grid[0].length; j++) {
        const element = this.grid[i][j];
        element.f = 0;
        element.g = 0;
        element.h = 0;
        element.isPath = false;
        element.parent = null;
      }
    }
  }

  run(
    source: Cell,
    target: Cell,
    algoritm: "manhattanDistance" | "euclideanDistance",
    type: "predador" | "presa"
  ): [Cell[] | null, Set<Cell> | null, boolean] {
    const openSet = [source];
    const closedSet = new Set<Cell>();

    let amountOfSteps = type === "predador" ? 2 : 1;

    while (openSet.length > 0) {
      let current = openSet[0];

      // Buscar o no que tenha o menor custo para explorar para o tipo predador
      for (let i = 1; i < openSet.length; i++) {
        if (
          (type === "presa" && openSet[i].h > current.h) ||
          (type === "predador" && openSet[i].f < current.f)
        ) {
          current = openSet[i];
        }
      }

      openSet.splice(openSet.indexOf(current), 1);
      closedSet.add(current);

      if (current === target) {
        let path: Cell[] = [];
        let temp = current;

        if (type === "predador") {
          while (temp) {
            path.push(temp);
            temp = temp.parent;
          }

          let newPath = path.reverse().splice(0, 3);

          if (newPath.length === 3) {
            for (let index = 0; index < newPath.length; index++) {
              const element = newPath[index];
              if (index === 0) {
                element.isSource = false;
              } else if (index === newPath.length - 1) {
                element.isSource = true;
                continue;
              }
              element.isPath = true;
            }

            const wasFound = newPath[newPath.length - 1] === target;
            return [newPath, closedSet, wasFound];
          }
        }

        path = [];
        temp = current;

        while (temp) {
          path.push(temp);
          temp = temp.parent;
          if (temp !== null && temp !== source) {
            temp.isPath = true;
          }
        }

        const wasFound = true;
        return [path.reverse(), closedSet, wasFound];
      }

      if (amountOfSteps <= 0 && type === "presa") {
        const path = [];

        let temp = current;

        temp.isTarget = true;
        path.push(temp);

        temp = temp.parent;
        temp.isTarget = false;
        temp.isPath = true;

        path.push(temp);

        const wasFound = false;
        return [path.reverse(), closedSet, wasFound];
      }

      const { row, column } = current;

      const successors = [
        { newRow: row - 1, newColumn: column, cost: 10 }, // top
        { newRow: row + 1, newColumn: column, cost: 10 }, // bottom
        { newRow: row, newColumn: column - 1, cost: 10 }, // left
        { newRow: row, newColumn: column + 1, cost: 10 }, // right
        { newRow: row - 1, newColumn: column - 1, cost: 14 }, // top | left
        { newRow: row - 1, newColumn: column + 1, cost: 14 }, // top | right
        { newRow: row + 1, newColumn: column - 1, cost: 14 }, // bottom | left
        { newRow: row + 1, newColumn: column + 1, cost: 14 }, // bottom | right
      ];

      for (const { newRow, newColumn, cost } of successors) {
        if (
          newRow >= 0 &&
          newRow < this.grid.length &&
          newColumn >= 0 &&
          newColumn < this.grid[0].length
        ) {
          const neighbor = this.grid[newRow][newColumn];
          if (!neighbor.isBlocked && !closedSet.has(neighbor)) {
            const tempG = current.g + cost;

            if (!openSet.includes(neighbor) || tempG < neighbor.g) {
              neighbor.g = tempG;
              neighbor.h = neighbor[algoritm](target);
              neighbor.f = neighbor.g + neighbor.h;
              neighbor.parent = current;

              if (!openSet.includes(neighbor)) {
                openSet.push(neighbor);
              }
            }
          }
        }
      }

      --amountOfSteps;
    }

    const wasFound = false;
    return [null, null, wasFound];
  }
}

export default function useAStarSearch() {
  const [gridState, setGridState] = useState<Cell[][]>([]);
  const [config, setConfig] = useState<ConfigTypes>({
    sourceWasChosen: false,
    targetWasChosen: false,
    wasFound: false,
    processFinished: false,
    sourceIndex: { row: 0, column: 0 },
    targetIndex: { row: 0, column: 0 },
    size: { row: 0, column: 0 },
    algoritm: "manhattanDistance",
  });

  useEffect(() => {
    if (config.size.row && config.size.column && !config.sourceWasChosen) {
      setGridState(
        new Array(config.size.row)
          .fill(null)
          .map((_, row) =>
            new Array(config.size.column)
              .fill(null)
              .map((_, column) => new Cell(row, column, false, false, false))
          )
      );
    }
  }, [config]);

  function handleChangeCellStatus(
    rowNumber: number,
    columnNumber: number,
    statusValue = true
  ) {
    const { sourceWasChosen, targetWasChosen } = config;

    if (!sourceWasChosen) {
      setGridState((prev) => {
        const newGrid = [...prev];

        newGrid[rowNumber][columnNumber].isSource = true;
        newGrid[rowNumber][columnNumber].f = 0;
        newGrid[rowNumber][columnNumber].g = 0;
        newGrid[rowNumber][columnNumber].h = 0;

        return newGrid;
      });
      setConfig((prev) => ({
        ...prev,
        sourceWasChosen: true,
        sourceIndex: { row: rowNumber, column: columnNumber },
      }));
    }

    //
    else if (!targetWasChosen && !gridState[rowNumber][columnNumber].isSource) {
      setGridState((prev) => {
        const newGrid = [...prev];

        newGrid[rowNumber][columnNumber].isTarget = true;

        return newGrid;
      });
      setConfig((prev) => ({
        ...prev,
        targetWasChosen: true,
        targetIndex: { row: rowNumber, column: columnNumber },
      }));
    }

    //
    else {
      if (
        !gridState[rowNumber][columnNumber].isSource ||
        !gridState[rowNumber][columnNumber].isTarget
      ) {
        setGridState((prev) => {
          const newGrid = [...prev];

          newGrid[rowNumber][columnNumber].isBlocked = statusValue;
          return newGrid;
        });
      }
    }
  }

  async function run() {
    const grid = [...gridState];
    // console.log(config.sourceIndex, config.targetIndex)

    let predador = grid[config.sourceIndex.row][config.sourceIndex.column];
    let presa = grid[config.targetIndex.row][config.targetIndex.column];
    let typeStep: "predador" | "presa" = "predador";

    const astar = new AStar(grid);
    let wasFound = false;

    print_out(grid);

    async function sleep(ms: number): Promise<void> {
      return new Promise((resolve) => setTimeout(resolve, ms));
    }

    while (!wasFound) {
      const [path, closedSet, wasFoundRet] = astar.run(
        typeStep === "predador" ? predador : presa,
        typeStep === "predador" ? presa : predador,
        "manhattanDistance",
        typeStep
      );

      predador = astar.getGridItemByType("predador") as Cell;
      presa = astar.getGridItemByType("presa") as Cell;

      setGridState([...grid]);

      await sleep(2000);

      console.log(predador.getPosition());
      console.log(presa.getPosition());
      astar.clearGrid();

      print_out(grid, typeStep === "predador" ? "PREDADOR" : "PRESA");

      wasFound = wasFoundRet;
      if (wasFoundRet) {
        setConfig((prev) => ({
          ...prev,
          processFinished: true,
          wasFound: wasFoundRet,
        }));
      }

      if (path === null) {
        console.log("Não encontrado!!!");
        setConfig((prev) => ({
          ...prev,
          processFinished: true,
          wasFound: wasFoundRet,
        }));
        break;
      }

      if (typeStep === "predador") {
        typeStep = "presa";
      } else {
        typeStep = "predador";
      }
    }
  }

  return {
    gridState,
    setConfig,
    run,
    handleChangeCellStatus,
    wasFound: config.wasFound,
    processFinished: config.processFinished,
  };
}
