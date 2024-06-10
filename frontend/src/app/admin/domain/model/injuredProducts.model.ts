export class InjuredProducts {
  constructor(
    public id: string,
    public name: string,
    public averageDays: number,
    public color?: string
  ) {}
}