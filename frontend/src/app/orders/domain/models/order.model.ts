import { DeliveredAddressModel } from "../../../organization/domain/models/deliveredAddress.model";
import { OrderStatus } from "../../infrastructure/dto/order.dto";

export class Order {
  constructor(
    public id: string,
    public totalPrice: number,
    public quantity: number,
    public providerId: string,
    public status: OrderStatus,
    public isPaid: boolean,
    public isActive: boolean,
    public paidDate: string,
    public realPaidDate: string,
    public number: number,
    public deliveredTotalDays: number,
    public deliveredAddressId: string,
    public realDeliveredDate: Date,
    public reasonCancelled: string,
    public deliveredOnTime: boolean,
    public updatedAt: Date,
    public createdAt: Date,
    public deliveredDate: string,
    public address?: DeliveredAddressModel
  ) {}

}

