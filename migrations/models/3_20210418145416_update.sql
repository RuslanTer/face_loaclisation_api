-- upgrade --
ALTER TABLE "image" ADD "description" TEXT NOT NULL;
ALTER TABLE "image" ALTER COLUMN "user_id" TYPE INT USING "user_id"::INT;
-- downgrade --
ALTER TABLE "image" DROP COLUMN "description";
ALTER TABLE "image" ALTER COLUMN "user_id" TYPE INT USING "user_id"::INT;
