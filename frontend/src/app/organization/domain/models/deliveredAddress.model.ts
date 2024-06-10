export class DeliveredAddressModel {
  constructor(
    public id: string,
    public country: string,
    public street: string,
    public cologne: string,
    public state: string,
    public extNum: number,
    public intNum: number,
    public pc: string,
    public organizationId: string,
    public isActive: boolean,
    public createdAt: string,
    public updatedAt: string
  ) {}
}
