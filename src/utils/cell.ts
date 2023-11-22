export default class Cell {
  row: number;
  column: number;
  isSource: boolean;
  isTarget: boolean;
  isBlocked: boolean;
  isPath: boolean;
  g: number;
  h: number;
  f: number;
  parent: any;

  constructor(
    row: number,
    column: number,
    isSource: boolean,
    isTarget: boolean,
    isBlocked: boolean
  ) {
    this.row = row;
    this.column = column;
    this.isSource = isSource;
    this.isTarget = isTarget;
    this.isBlocked = isBlocked;
    this.isPath = false;

    this.g = 0; // distância da célula inicial até esta
    this.h = 0; // heurística - estimativa da distância até o destino
    this.f = 0; // custo total: F = G + H
    this.parent = null;
  }

  manhattanDistance(target: Cell) {
    return (
      Math.abs(this.row - target.row) + Math.abs(this.column - target.column)
    );
  }

  euclideanDistance(target: Cell) {
    const dx = this.row - target.row;
    const dy = this.column - target.column;
    return Math.sqrt(dx * dx + dy * dy);
  }

  getPosition() {
    return `row: ${this.row} column: ${this.column}`;
  }

  toString() {
    if (this.isBlocked) {
      return `B ${this.g} ${this.h} ${this.f}`;
    } else if (this.isTarget) {
      return `T ${this.g} ${this.h} ${this.f}`;
    } else if (this.isSource) {
      return `S ${this.g} ${this.h} ${this.f}`;
    }
    return `0 ${this.g} ${this.h} ${this.f}`;
  }
}
