---- Add users
--
-- Putin
INSERT INTO users VALUES (
  'putin',
  'Vladimir',
  'Putin'
);
-- B J
INSERT INTO users VALUES (
  'bj',
  'B',
  'J'
);
-- Zelensky
INSERT INTO users VALUES (
  'zelensky',
  'Volodymyr',
  'Zelensky'
);

---- Add incomes
-- Putin
INSERT INTO income VALUES (
  'putin-oil',
  'putin',
  'Oil',
  1000000000
);
INSERT INTO income VALUES (
  'putin-extortion',
  'putin',
  'Extortion',
  137000833
);
INSERT INTO income VALUES (
  'putin-child-trafficking',
  'putin',
  'Child trafficking',
  5000000
);
-- B J
INSERT INTO income VALUES (
  'bj-human-trafficking',
  'bj',
  'Human trafficking',
  1000000000
);
INSERT INTO income VALUES (
  'bj-enslaving',
  'bj',
  'Enslaving',
  1000000532
);
INSERT INTO income VALUES (
  'bj-covid',
  'bj',
  'Covid',
  2000000000
);
INSERT INTO income VALUES (
  'bj-statization',
  'bj',
  'Statization',
  2147483647
);
-- Zelensky
INSERT INTO income VALUES (
  'zelensky-salary',
  'zelensky',
  'Presidential salary',
  5000
);

----Add expenses----
INSERT INTO expense VALUES (
'mercado',
'daniel',
'compras do mês',
453.21
);