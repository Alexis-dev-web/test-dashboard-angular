import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MaterialSectionComponent } from './material-section.component';

describe('MaterialSectionComponent', () => {
  let component: MaterialSectionComponent;
  let fixture: ComponentFixture<MaterialSectionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MaterialSectionComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(MaterialSectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
