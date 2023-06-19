---- Add users
--
-- Putin
INSERT INTO users VALUES (
  'putin',
  'Vladimir Putin',
  'vlad@gg.com'
);
-- B J
INSERT INTO users VALUES (
  'bj',
  'B J',
  'bj@gg.com'
);
-- Zelensky
INSERT INTO users VALUES (
  'zelensky',
  'Volodymyr Zelensky',
  'volodo@gg.com'
);

-- Daniel
INSERT INTO users VALUES (
  'daniel',
  'Daniel Campos',
  'dan@gg.com'
);

-- Leticia
INSERT INTO users VALUES (
  'leticia',
  'Leticia Alves',
  'leticia@email.com',
  '123'
);

---- Add incomes
-- Putin
INSERT INTO income VALUES (
  'putin-oil',
  'putin',
  'Oil',
  10000,
  '2023-01-1'
);
INSERT INTO income VALUES (
  'putin-extortion',
  'putin',
  'Extortion',
  1370,
  '2023-02-1'
);
INSERT INTO income VALUES (
  'putin-child-trafficking',
  'putin',
  'Child trafficking',
  5000,
  '2023-03-1'
);
-- B J
INSERT INTO income VALUES (
  'bj-human-trafficking',
  'bj',
  'Human trafficking',
  10000,
  '2023-01-01'
);
INSERT INTO income VALUES (
  'bj-enslaving',
  'bj',
  'Enslaving',
  10532,
  '2023-02-01'
);
INSERT INTO income VALUES (
  'bj-covid',
  'bj',
  'Covid',
  2000,
  '2023-03-01'
);
INSERT INTO income VALUES (
  'bj-statization',
  'bj',
  'Statization',
  23647,
  '2023-04-01'
);
-- Zelensky
INSERT INTO income VALUES (
  'zelensky-salary',
  'zelensky',
  'Presidential salary',
  5000,
  '2023-02-01'
);
-- Daniel
INSERT INTO income VALUES (
  'inc_1',
  'daniel',
  'Bolsa de Projeto',
  1000,
  '2023-02-01'
);

INSERT INTO income VALUES (
  'inc_2',
  'daniel',
  'Investimentos',
  5000,
  '2023-02-17'
);

INSERT INTO income VALUES (
  'inc_3',
  'daniel',
  'Mega-Sena',
  7000,
  '2023-02-29'
);

INSERT INTO income VALUES (
  'inc_4',
  'daniel',
  'Bolsa de Projeto',
  1000,
  '2023-03-01'
);

INSERT INTO income VALUES (
  'inc_5',
  'daniel',
  'Investimentos',
  2000,
  '2023-03-17'
);

INSERT INTO income VALUES (
  'inc_6',
  'daniel',
  'Mega-Sena',
  7500,
  '2023-03-29'
);


----Add expenses----
INSERT INTO expense VALUES (
'exp_id123',
'daniel',
'compras do mês',
453.21,
'2023-01-01'
);

INSERT INTO expense VALUES (
'exp_id124',
'daniel',
'compras do mês',
60,
'2023-02-01'
);

INSERT INTO expense VALUES (
'exp_1',
'daniel',
'EPA',
60,
'2023-02-01'
);

INSERT INTO expense VALUES (
'exp_2',
'daniel',
'Padaria',
15,
'2023-02-06'
);

INSERT INTO expense VALUES (
'exp_3',
'daniel',
'Farmácia',
30,
'2023-02-17'
);

INSERT INTO expense VALUES (
'exp_4',
'daniel',
'EPA',
140,
'2023-03-01'
);

INSERT INTO expense VALUES (
'exp_5',
'daniel',
'Padaria',
25,
'2023-03-06'
);

INSERT INTO expense VALUES (
'exp_6',
'daniel',
'Farmácia',
10,
'2023-03-17'
);

INSERT INTO expense VALUES (
'exp_id333',
'yowgf',
'wasting money',
999.99,
'2023-03-24'
);

----Add expenses tag-----
INSERT INTO expense_tag VALUES (
'exp_id123',
'mercado'
);
INSERT INTO expense_tag VALUES (
'exp_5',
'mercado'
);
INSERT INTO expense_tag VALUES (
'exp_id123',
'compra-de-ovos'
);
INSERT INTO expense_tag VALUES (
'exp_3',
'farmacia'
);
INSERT INTO expense_tag VALUES (
'exp_6',
'farmacia'
);
