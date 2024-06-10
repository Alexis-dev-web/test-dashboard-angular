import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CompletedAdvanceComponent } from './completed-advance.component';

describe('CompletedAdvanceComponent', () => {
  let component: CompletedAdvanceComponent;
  let fixture: ComponentFixture<CompletedAdvanceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CompletedAdvanceComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CompletedAdvanceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
