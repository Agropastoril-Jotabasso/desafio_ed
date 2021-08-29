-- Table: public.fato_orcamento

-- DROP TABLE public.fato_orcamento;

CREATE TABLE public.fato_orcamento
(
    id integer NOT NULL,
    filial character varying(4) COLLATE pg_catalog."default",
    setor character varying(10) COLLATE pg_catalog."default",
    dt_orcamento date,
    valor numeric(18,3),
    CONSTRAINT fato_orcamento_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.fato_orcamento
    OWNER to postgres;