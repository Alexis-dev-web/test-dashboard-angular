export class ProviderDelivered {
  constructor(
    public id: string,
    public name: string,
    public averageDays: number,
    public color?: string
  ) {}
}