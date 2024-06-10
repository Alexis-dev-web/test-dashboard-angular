export enum Gender {
  male,
  female
}

export enum UserType {
  ADMIN,
  NORMAL,
  SELLER,
  CLIENT,
}

export class User {
  constructor(
    public id: string,
    public name: string,
    public last_name: string,
    public email: string,
    public gender: Gender,
    public is_active: boolean,
    public is_superuser: boolean,
    public role: UserType,
    public created_at: string,
    public updated_at: string,
    public last_login: string
  ) {}
}