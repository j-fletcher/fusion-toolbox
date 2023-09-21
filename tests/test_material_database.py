from pathlib import Path


def test_material_save_to(tmp_path):
    "test the method that stores data of a Material object"
    from fusion_toolbox.materials.material_constructor import Material

    d = tmp_path

    filename = str(d / 'test_mat_database.pkl')
    p = Path(filename)

    test_material = Material(
        name='test',
        composition='test',
        density=0.,
        thermal_conductivity=0.,
    )

    test_material.save_to(filename)

    assert p.exists()
