-- upgrade --
ALTER TABLE "image" ALTER COLUMN "image" TYPE BYTEA USING "image"::BYTEA;
ALTER TABLE "image" ALTER COLUMN "image" TYPE BYTEA USING "image"::BYTEA;
ALTER TABLE "image" ALTER COLUMN "image" TYPE BYTEA USING "image"::BYTEA;
ALTER TABLE "image" ALTER COLUMN "image" TYPE BYTEA USING "image"::BYTEA;
-- downgrade --
ALTER TABLE "image" ALTER COLUMN "image" TYPE VARCHAR(10) USING "image"::VARCHAR(10);
ALTER TABLE "image" ALTER COLUMN "image" TYPE VARCHAR(10) USING "image"::VARCHAR(10);
ALTER TABLE "image" ALTER COLUMN "image" TYPE VARCHAR(10) USING "image"::VARCHAR(10);
ALTER TABLE "image" ALTER COLUMN "image" TYPE VARCHAR(10) USING "image"::VARCHAR(10);