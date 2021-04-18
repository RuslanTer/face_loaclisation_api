-- upgrade --
CREATE TABLE IF NOT EXISTS "image" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "image" VARCHAR(10) NOT NULL,
    "stats" TEXT NOT NULL,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "image"."user_id" IS 'This is a username';
COMMENT ON TABLE "image" IS 'The image model';
-- downgrade --
DROP TABLE IF EXISTS "image";
