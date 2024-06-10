export enum OrderReportStatus {
  ACTIVE = 'Active',
  CANCELLED = 'Cancelled',
  DELIVERED = 'Completed',
  TOTAL = 'Total orders'
}

export class OrderStatusModel {
  constructor(
    public color: string,
    public title: string,
    public total: number
  ) {}
}
