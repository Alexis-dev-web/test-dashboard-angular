import { DeliveredAddressModel } from '../../domain/models/deliveredAddress.model';
import { DeliveredAddressDTO } from '../dto/deliveredAddress.dto';

export class DeliveredAddressMapper {
  static fromApiToDomain(address: DeliveredAddressDTO): DeliveredAddressModel {
    return {
      id: address.id,
      country: address.country,
      street: address.street,
      cologne: address.cologne,
      state: address.state,
      extNum: address.ext_num,
      intNum: address.int_num,
      pc: address.pc,
      organizationId: address.organization_id,
      isActive: address.is_active,
      createdAt: address.created_at,
      updatedAt: address.updated_at
    }
  }
}