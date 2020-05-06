export class Exam {
  constructor(
    public title: string,
    public description: string,
    public updatedAt: Date,
    public createdAt: Date,
    public _id?: number,
    public lastUpdatedBy?: string
  ) {}
}
