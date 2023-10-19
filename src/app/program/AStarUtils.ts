import { CellTypes } from '@/types/cell'

class AStarUtils {
  private NUMBER_OF_ROWS: number
  private NUMBER_OF_COLUMNS: number
  private TARGET_ROW_NUMBER: number
  private TARGET_COLUMN_NUMBER: number
  private GRID: CellTypes[][]

  constructor(
    grid: CellTypes[][],
    numberOfRows: number,
    numberOfColumns: number,
    targetRowNumber: number,
    targetColumnNumber: number,
  ) {
    this.NUMBER_OF_ROWS = numberOfRows
    this.NUMBER_OF_COLUMNS = numberOfColumns
    this.TARGET_ROW_NUMBER = targetRowNumber
    this.TARGET_COLUMN_NUMBER = targetColumnNumber
    this.GRID = grid
  }

  // Verifica se uma movimentação esta no range
  isValid(row: number, column: number) {
    return (
      row >= 0 &&
      row < this.NUMBER_OF_ROWS &&
      column >= 0 &&
      column < this.NUMBER_OF_COLUMNS
    )
  }

  isUnBlocked(row: number, column: number) {
    return !this.GRID[row][column].isBlocked
  }

  isTarget(row: number, column: number) {
    return this.GRID[row][column].isTarget
  }

  // Calcular o 'h' heuristics.
  calculateHValue(row: number, col: number) {
    return Math.sqrt(
      (row - this.TARGET_ROW_NUMBER) * (row - this.TARGET_ROW_NUMBER) +
        (col - this.TARGET_COLUMN_NUMBER) * (col - this.TARGET_COLUMN_NUMBER),
    )
  }

  // A Utility Function to trace the path from the source
  // to destination
  tracePath() {
    let row = this.TARGET_ROW_NUMBER
    let column = this.TARGET_COLUMN_NUMBER

    const Path = []

    while (
      !(
        this.GRID[row][column].parent_row === row &&
        this.GRID[row][column].parent_column === column
      )
    ) {
      Path.push([row, column])
      row = this.GRID[row][column].parent_row
      column = this.GRID[row][column].parent_column
    }

    Path.push([row, column])
    while (Path.length > 0) {
      const p = Path[0]
      Path.shift()

      if (p[0] === 2 || p[0] === 1) {
        console.log('-> (' + p[0] + ', ' + (p[1] - 1) + ')')
      } else console.log('-> (' + p[0] + ', ' + p[1] + ')')
    }
  }
}

export default AStarUtils
