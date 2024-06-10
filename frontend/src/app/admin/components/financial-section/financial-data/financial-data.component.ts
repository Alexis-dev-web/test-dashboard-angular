import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { MatCard, MatCardContent, MatCardTitle } from '@angular/material/card';
import { MatGridList, MatGridTile } from '@angular/material/grid-list';
import {
  ChartComponent,
  ApexAxisChartSeries,
  ApexChart,
  ApexXAxis,
  ApexDataLabels,
  ApexTooltip,
  ApexStroke,
  NgApexchartsModule,
  ApexLegend,
  ApexYAxis,
  ApexGrid
} from "ng-apexcharts";

export type ChartOptions = {
  series: ApexAxisChartSeries;
  chart: ApexChart;
  xaxis: ApexXAxis;
  stroke: ApexStroke;
  tooltip: ApexTooltip;
  dataLabels: ApexDataLabels;
  legend: ApexLegend;
  yaxis: ApexYAxis | ApexYAxis[];
  grid: ApexGrid
};


@Component({
  selector: 'app-financial-data',
  standalone: true,
  imports: [
    NgApexchartsModule,
    MatCard,
    MatCardTitle,
    MatCardContent,
    MatGridList,
    MatGridTile
  ],
  templateUrl: './financial-data.component.html',
  styleUrl: './financial-data.component.css'
})
export class FinancialDataComponent implements OnInit {
  @ViewChild("chart") chart!: ChartComponent;
  public chartOptions!: Partial<ChartOptions>;
  @Input() breakpoint!: number;

  constructor() {}
  ngOnInit(): void {
    this.chartOptions = {
      series: [
        {
          name: "series1",
          data: [31, 40, 28, 51, 42, 109, 100, 10, 50, 45, 56, 48],
          color: '#93C5FD'
        },
        {
          name: "series2",
          data: [11, 32, 45, 32, 34, 52, 41, 87, 100, 86, 24, 10],
          color: '#1D4ED8'
        }
      ],
      chart: {
        height: 350,
        type: "area",
        toolbar: {
          show: false
        },
      },
      legend: {
        show: false
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        curve: "monotoneCubic",
        width: 2
      },
      xaxis: {
        type: 'category',
        offsetY: -30,
        categories: [
          "Jun",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "Jun",
          "Jul",
          "Ago",
          "Sep",
          "Oct",
          "Nov",
          "Dec"
        ],
      },
      yaxis: {
        show: false
      },
      tooltip: {
        enabled: false
      },
      grid: {
        show: false
      }
    };
  }
  
  
}
