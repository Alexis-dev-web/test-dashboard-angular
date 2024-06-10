import { ProviderDelivered } from '../../domain/model/providerDelivered.model';
import { ProviderDeliveredDTO } from '../dto/providerDelivered.dto';

export class ProviderDeliveredMapper {
  static fromApiToDomain(
    providers: ProviderDeliveredDTO[]
  ): ProviderDelivered[] {
    var provider_delivery: ProviderDelivered[] = [];

    providers.map((provider) =>
      provider_delivery.push({
        id: provider.id,
        name: provider.name,
        averageDays: provider.average_days,
        color: undefined,
      })
    );
    return provider_delivery;
  }
}
