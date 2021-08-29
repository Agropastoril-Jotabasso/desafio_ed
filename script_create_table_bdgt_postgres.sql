-- Table: public.bdgt

-- DROP TABLE public.bdgt;

CREATE TABLE public.bdgt
(
    ast character varying(4) COLLATE pg_catalog."default" NOT NULL,
    sekt character varying(10) COLLATE pg_catalog."default",
    jahr character varying(4) COLLATE pg_catalog."default",
    monat01 numeric(18,3),
    monat02 numeric(18,3),
    monat03 numeric(18,3),
    monat04 numeric(18,3),
    monat05 numeric(18,3),
    monat06 numeric(18,3),
    monat07 numeric(18,3),
    monat08 numeric(18,3),
    monat09 numeric(18,3),
    monat10 numeric(18,3),
    monat11 numeric(18,3),
    monat12 numeric(18,3),
    CONSTRAINT bdgt_pkey PRIMARY KEY (ast)
)

TABLESPACE pg_default;

ALTER TABLE public.bdgt
    OWNER to postgres;