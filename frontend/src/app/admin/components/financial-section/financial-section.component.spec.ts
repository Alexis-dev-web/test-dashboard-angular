import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FinancialSectionComponent } from './financial-section.component';

describe('FinancialSectionComponent', () => {
  let component: FinancialSectionComponent;
  let fixture: ComponentFixture<FinancialSectionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FinancialSectionComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(FinancialSectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
