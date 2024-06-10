import { OrderByYear } from "../../domain/model/orderByYear.model";
import { OrderByYearDTO } from "../dto/orderByYear.dto";

export class OrderByYearMapper {
  static fromApiToDomain(years: OrderByYearDTO[]): OrderByYear[] {
    let response: OrderByYear[] = []
    years.map((year) => {
      response.push({
        year: year.year,
        totalDelivered: year.total_delivered
      })
    })

    return response
  }
}