create table if not exists users (
  id char(32),
  name char(32),
  email char(64),
  password char(32),
  PRIMARY KEY(id)
);

create table if not exists income (
  id char(32),
  user_id char(32),
  src char(32),
  amount real,
  inc_date date,
  PRIMARY KEY(id)
);

create table if not exists expense (
  id char(32),
  user_id char(32),
  src char(32),
  amount real,
  exp_date date,
  PRIMARY KEY(id)
);

create table if not exists expense_tag (
  expense_id char(32),
  tag_name char(32),
  CONSTRAINT fk_expense
      FOREIGN KEY(expense_id) 
	      REFERENCES expense(id)
);
