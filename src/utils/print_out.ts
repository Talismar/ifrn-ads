import Cell from "./cell";

export function print_out(grid: Cell[][], message: string = "GRID Inicial") {
  console.log("---------");
  console.log(message);
  console.log("---------");

  for (let i = 0; i < grid.length; i++) {
    let rowValues = "";
    for (let j = 0; j < grid[0].length; j++) {
      const element = grid[i][j];

      if (element.isBlocked) {
        rowValues += ` B`;
      } else if (element.isSource) {
        rowValues += " S";
      } else if (element.isTarget) {
        rowValues += " T";
      } else if (element.isPath) {
        rowValues += " P";
      } else {
        rowValues += " 0";
      }
      // rowValues += ` ${element} |`;
    }

    console.log(rowValues);
  }
  console.log();
}
