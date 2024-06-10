import { Observable } from 'rxjs';

import { User } from '../models/user.model';
import { Auth } from '../models/auth.model';


export abstract class AuthRepository {
  abstract login(): Observable<Auth[]>;
  abstract refreshToken(): Observable<Auth[]>;
}