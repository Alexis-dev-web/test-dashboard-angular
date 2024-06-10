import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, map } from 'rxjs';
import { ReportOrdersDTO } from '../dto/reportOrders.dto';
import { environment } from '../../../../environments/environment';
import { OrderReportMapper } from '../mappers/orderReport.mapper';
import { OrderReport } from '../../domain/model/reportOrder.model';

@Injectable({
  providedIn: 'root'
})
export class ReportService {
  private apiUrl = environment.production ? `${environment.baseUrl}/orders/report` : `/api/api/orders/report`;
  private headers = new HttpHeaders({'Content-Type': 'application/json; charset=utf-8', 'Access-Control-Allow-Origin': '*'});

  constructor(private http: HttpClient) {}

  getReport(): Observable<OrderReport> {
    return this.http
      .get<ReportOrdersDTO>(this.apiUrl, { headers: this.headers})
      .pipe(map(OrderReportMapper.fromApiToDomain))
  }
}
