import { Injectable } from '@angular/core';
import { UseCaseOnlyOutput } from '../../../core/useCases/onlyOutput.useCase';
import { Observable } from 'rxjs';
import { OrderReport } from '../model/reportOrder.model';
import { ReportsRepositoryImpl } from '../repositories/reports.reporitory.impl';

@Injectable({
  providedIn: 'root'
})
export class GetOrderReport implements UseCaseOnlyOutput {
  constructor(private reportRepository: ReportsRepositoryImpl) {}

  run(): Observable<OrderReport> {
    try {
      return this.reportRepository.getOrderReport()
    } catch (error) {
      console.error('Error al cargar las tareas:', error);
      throw error;
    }
  }
}
