import { Observable } from 'rxjs';

export abstract class UseCaseOnlyOutput {
  abstract run(): any;
}