import { Observable } from 'rxjs';

import { OrderReport } from '../model/reportOrder.model';

export abstract class ReportsRepository {
  abstract getOrderReport(): Observable<OrderReport>;
}
