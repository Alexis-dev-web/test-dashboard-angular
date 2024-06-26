import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CardNumberComponent } from './card-number.component';

describe('CardNumberComponent', () => {
  let component: CardNumberComponent;
  let fixture: ComponentFixture<CardNumberComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CardNumberComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CardNumberComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
