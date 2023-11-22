export type IndexTypes = { row: number; column: number };
export type ConfigTypes = {
  sourceWasChosen: boolean;
  targetWasChosen: boolean;
  wasFound: boolean;
  processFinished: boolean;
  sourceIndex: IndexTypes;
  targetIndex: IndexTypes;
  size: IndexTypes;
  algoritm: "manhattanDistance" | "euclideanDistance";
};
