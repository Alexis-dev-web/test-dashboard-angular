import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TransitChartComponent } from './transit-chart.component';

describe('TransitChartComponent', () => {
  let component: TransitChartComponent;
  let fixture: ComponentFixture<TransitChartComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TransitChartComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(TransitChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
