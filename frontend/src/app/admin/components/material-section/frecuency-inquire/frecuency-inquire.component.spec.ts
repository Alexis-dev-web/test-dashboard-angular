import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FrecuencyInquireComponent } from './frecuency-inquire.component';

describe('FrecuencyInquireComponent', () => {
  let component: FrecuencyInquireComponent;
  let fixture: ComponentFixture<FrecuencyInquireComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FrecuencyInquireComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(FrecuencyInquireComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
