/* eslint-disable camelcase */
const ROW = 9
const COL = 10

class Cell {
  public parent_i: number
  public parent_j: number
  public f: number, g: number, h: number
  constructor(
    parent_i: number,
    parent_j: number,
    f: number,
    g: number,
    h: number,
  ) {
    this.parent_i = parent_i
    this.parent_j = parent_j
    this.f = f
    this.g = g
    this.h = h
  }
}

class AStar {
  isValid(row, col) {
    return row >= 0 && row < ROW && col >= 0 && col < COL
  }

  isUnBlocked(grid, row, col) {
    return grid[row][col] === 1
  }

  isDestination(row, col, dest) {
    return row === dest[0] && col === dest[1]
  }

  calculateHValue(row, col, dest) {
    return Math.sqrt((row - dest[0]) ** 2 + (col - dest[1]) ** 2)
  }

  tracePath(cellDetails, dest) {
    console.log('The Path is ')
    const path = []
    let row = dest[0]
    let col = dest[1]

    while (
      !(
        cellDetails[row][col].parent_i === row &&
        cellDetails[row][col].parent_j === col
      )
    ) {
      path.push([row, col])
      const temp_row = cellDetails[row][col].parent_i
      const temp_col = cellDetails[row][col].parent_j
      row = temp_row
      col = temp_col
    }

    path.push([row, col])
    path.reverse()

    for (const p of path) {
      const outputRow = p[0]
      const outputCol = p[1]
      console.log(`-> (${outputRow}, ${outputCol})`)
    }
  }

  aStarSearch(src, dest) {
    if (!isValid(src[0], src[1]) || !isValid(dest[0], dest[1])) {
      console.log('Source or destination is invalid')
      return
    }

    if (
      !isUnBlocked(grid, src[0], src[1]) ||
      !isUnBlocked(grid, dest[0], dest[1])
    ) {
      console.log('Source or destination is blocked')
      return
    }

    if (isDestination(src[0], src[1], dest)) {
      console.log('We are already at the destination')
      return
    }

    const closedList = new Array(ROW)
      .fill(null)
      .map(() => new Array(COL).fill(false))
    const cellDetails = new Array(ROW)
      .fill(null)
      .map(() => new Array(COL).fill(null))

    for (let i = 0; i < ROW; i++) {
      for (let j = 0; j < COL; j++) {
        cellDetails[i][j] = new Cell(-1, -1, -1, -1, -1)
      }
    }

    const [i, j] = src
    cellDetails[i][j] = new Cell(i, j, 0, 0, 0)

    const openList = new Map()
    openList.set(0, [i, j])

    let foundDest = false

    while (openList.size > 0) {
      const [f, [i, j]] = openList.entries().next().value
      openList.delete(f)
      closedList[i][j] = true

      const successors = [
        { row: i - 1, column: j, cost: 10 },
        { row: i + 1, column: j, cost: 10 },
        { row: i, column: j + 1, cost: 10 },
        { row: i, column: j - 1, cost: 10 },
        { row: i - 1, column: j + 1, cost: 10 },
        { row: i - 1, column: j - 1, cost: 10 },
        { row: i + 1, column: j + 1, cost: 10 },
        { row: i + 1, column: j - 1, cost: 10 },
      ]

      for (const { row, column, cost } of successors) {
        if (isValid(row, column)) {
          if (isDestination(row, column, dest)) {
            cellDetails[row][column].parent_i = i
            cellDetails[row][column].parent_j = j
            console.log('The destination cell is found')
            console.log(cellDetails)
            tracePath(cellDetails, dest)
            foundDest = true
            return
          } else if (
            !closedList[row][column] &&
            isUnBlocked(grid, row, column)
          ) {
            const gNew = cellDetails[i][j].g + cost
            const hNew = calculateHValue(row, column, dest)
            const fNew = gNew + hNew

            if (
              cellDetails[row][column].f === -1 ||
              cellDetails[row][column].f > fNew
            ) {
              openList.set(fNew, [row, column])
              cellDetails[row][column] = new Cell(i, j, fNew, gNew, hNew)
            }
          }
        }
      }
    }

    if (!foundDest) {
      throw new Error("Sem caminho");
    }
  }
}
