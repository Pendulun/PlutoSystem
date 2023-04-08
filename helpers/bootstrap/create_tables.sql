create table if not exists users (
  id char(32),
  first_name char(32),
  last_name char(32)
);

create table if not exists income (
  id char(32),
  user_id char(32),
  src char(32),
  amount bigint
);
