-- upgrade --
CREATE TABLE IF NOT EXISTS "faces" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "box" TEXT NOT NULL,
    "confidence" DOUBLE PRECISION NOT NULL,
    "left_eye" TEXT NOT NULL,
    "right_eye" TEXT NOT NULL,
    "nose" TEXT NOT NULL,
    "mouth_left" TEXT NOT NULL,
    "mouth_right" TEXT NOT NULL,
    "image_id" INT NOT NULL REFERENCES "image" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "faces" IS 'The face info model';;
ALTER TABLE "image" DROP COLUMN "stats";
-- downgrade --
ALTER TABLE "image" ADD "stats" TEXT NOT NULL;
DROP TABLE IF EXISTS "faces";
