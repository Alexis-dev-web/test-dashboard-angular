import { DeliveredAddressDTO } from "../../../organization/infraestructure/dto/deliveredAddress.dto";

export enum OrderStatus {
  CREATE,
  CANCELLED,
  DELIVERED,
}

export interface OrderDTO {
  id: string;
  total_price: number;
  quantity: number;
  provider_id: string;
  status: OrderStatus;
  is_paid: boolean;
  is_active: boolean;
  paid_date: string;
  real_paid_date: string;
  number: number;
  delivered_total_days: number;
  delivered_address_id: string;
  real_delivered_date: Date;
  reason_cancelled: string;
  delivered_on_time: boolean;
  delivered_date: string;
  updated_at: Date;
  created_at: Date;
  address?: DeliveredAddressDTO;
}
