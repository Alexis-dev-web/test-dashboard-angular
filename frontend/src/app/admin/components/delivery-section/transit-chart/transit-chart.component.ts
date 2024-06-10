import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { NgApexchartsModule } from 'ng-apexcharts';

import {
  ChartComponent,
  ApexAxisChartSeries,
  ApexChart,
  ApexFill,
  ApexYAxis,
  ApexTooltip,
  ApexTitleSubtitle,
  ApexXAxis,
  ApexPlotOptions,
  ApexLegend,
} from "ng-apexcharts";
import { OrderByYear } from '../../../domain/model/orderByYear.model';

export type ChartOptions = {
  series: ApexAxisChartSeries;
  chart: ApexChart;
  xaxis: ApexXAxis;
  yaxis: ApexYAxis | ApexYAxis[];
  title: ApexTitleSubtitle;
  labels: string[];
  stroke: any; // ApexStroke;
  dataLabels: any; // ApexDataLabels;
  fill: ApexFill;
  tooltip: ApexTooltip;
  plotOptions: ApexPlotOptions;
  legend: ApexLegend;
  colors: any;
}

@Component({
  selector: 'app-transit-chart',
  standalone: true,
  imports: [NgApexchartsModule],
  templateUrl: './transit-chart.component.html',
  styleUrl: './transit-chart.component.css'
})

export class TransitChartComponent implements OnInit {
  @ViewChild("chart") chart!: ChartComponent;
  @Input() years!: OrderByYear[];
  labels: string[] = [];
  values: number[] = [];
  colors: string[] = []; 

  public chartOptions!: Partial<ChartOptions>;

  constructor() { }

  ngOnInit(): void {
    const today = new Date().getFullYear()

    this.years.map((year) => {
      this.values.push(year.totalDelivered)

      this.labels.push(year.year.toString() === today.toString() ? 'Actual' : year.year)
    })

    this.chartOptions = {
      series: [
        {
          type: "column",
          data: this.values,
          
        },
        {
          type: "line",
          data: this.values,
          color: '#64748B'
        }
      ],
      chart: {
        height: 320,
        type: "line",
        toolbar: {
          show: false
        },
        
      },
      stroke: {
        width: [0.5, 3]
      },
      dataLabels: {
        enabled: true,
        enabledOnSeries: [1, 1],
        style: {
          colors: [
            ({value, seriesIndex, dataPointIndex, w}: any) => {
              const labels = w.globals.categoryLabels;
              if (labels[dataPointIndex] === 'Actual') {
                return '#01A696';
              } 
    
              return '#64748B'
            }, 
          ]
        }
      },
      labels: this.labels,
      plotOptions: {
        bar: {
          columnWidth: 33.76,
        },
      },
      yaxis: {
        min: 0,
        stepSize: 9,
      },
      tooltip: {
        enabled: false,
      },
      legend: {
        show: false
      },
      xaxis: {
        categories: this.labels
      },
      colors: [
        ({value, seriesIndex, dataPointIndex, w}: any) => {
          const labels = w.globals.categoryLabels;
          if (labels[dataPointIndex] === 'Actual') {
            return '#E6FEFC';
          } 

          return 'gray'
        }, 
      ]
    };
  }
}
