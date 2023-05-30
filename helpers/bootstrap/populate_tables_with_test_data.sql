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

-- Daniel
INSERT INTO users VALUES (
  'daniel',
  'Daniel',
  'Campos'
);

---- Add incomes
-- Putin
INSERT INTO income VALUES (
  'putin-oil',
  'putin',
  'Oil',
  10000,
  '1/01/2023'
);
INSERT INTO income VALUES (
  'putin-extortion',
  'putin',
  'Extortion',
  1370,
  '1/02/2023'
);
INSERT INTO income VALUES (
  'putin-child-trafficking',
  'putin',
  'Child trafficking',
  5000,
  '1/03/2023'
);
-- B J
INSERT INTO income VALUES (
  'bj-human-trafficking',
  'bj',
  'Human trafficking',
  10000,
  '01/01/2023'
);
INSERT INTO income VALUES (
  'bj-enslaving',
  'bj',
  'Enslaving',
  10532,
  '01/02/2023'
);
INSERT INTO income VALUES (
  'bj-covid',
  'bj',
  'Covid',
  2000,
  '01/03/2023'
);
INSERT INTO income VALUES (
  'bj-statization',
  'bj',
  'Statization',
  23647,
  '01/04/2023'
);
-- Zelensky
INSERT INTO income VALUES (
  'zelensky-salary',
  'zelensky',
  'Presidential salary',
  5000,
  '01/02/2023'
);
-- Daniel
INSERT INTO income VALUES (
  'inc_1',
  'daniel',
  'Bolsa de Projeto',
  1000,
  '01/02/2023'
);

INSERT INTO income VALUES (
  'inc_2',
  'daniel',
  'Investimentos',
  5000,
  '17/02/2023'
);

INSERT INTO income VALUES (
  'inc_3',
  'daniel',
  'Mega-Sena',
  7000,
  '29/02/2023'
);

INSERT INTO income VALUES (
  'inc_4',
  'daniel',
  'Bolsa de Projeto',
  1000,
  '01/03/2023'
);

INSERT INTO income VALUES (
  'inc_5',
  'daniel',
  'Investimentos',
  2000,
  '17/03/2023'
);

INSERT INTO income VALUES (
  'inc_6',
  'daniel',
  'Mega-Sena',
  7500,
  '29/03/2023'
);


----Add expenses----
INSERT INTO expense VALUES (
'exp_id123',
'daniel',
'compras do mês',
453.21,
'01/01/2023'
);

INSERT INTO expense VALUES (
'exp_id124',
'daniel',
'compras do mês',
60,
'01/02/2023'
);

INSERT INTO expense VALUES (
'exp_1',
'daniel',
'EPA',
60,
'01/02/2023'
);

INSERT INTO expense VALUES (
'exp_2',
'daniel',
'Padaria',
15,
'06/02/2023'
);

INSERT INTO expense VALUES (
'exp_3',
'daniel',
'Farmácia',
30,
'17/02/2023'
);

INSERT INTO expense VALUES (
'exp_4',
'daniel',
'EPA',
140,
'01/03/2023'
);

INSERT INTO expense VALUES (
'exp_5',
'daniel',
'Padaria',
25,
'06/03/2023'
);

INSERT INTO expense VALUES (
'exp_6',
'daniel',
'Farmácia',
10,
'17/03/2023'
);

INSERT INTO expense VALUES (
'exp_id333',
'yowgf',
'wasting money',
999.99,
'24/03/2023'
);

----Add expenses tag-----
INSERT INTO expense_tag VALUES (
'exp_id123',
'mercado'
);
INSERT INTO expense_tag VALUES (
'exp_id123',
'compra-de-ovos'
);
