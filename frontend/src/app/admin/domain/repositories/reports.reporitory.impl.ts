import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ReportsRepository } from './reports.repository';
import { OrderReport } from '../model/reportOrder.model';
import { ReportService } from '../../infraestructure/services/reports.repository';

@Injectable({
  providedIn: 'root'
})
export class ReportsRepositoryImpl implements ReportsRepository {
  constructor(private reportService: ReportService) {}

  getOrderReport(): Observable<OrderReport> {
    return this.reportService.getReport();
  }
}
