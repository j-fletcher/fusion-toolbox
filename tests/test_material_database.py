import os.path


def test_material_save_to(tmp_path):
    "test the method that stores data of a Material object"
    from fusion_toolbox.material_constructor import Material

    d = tmp_path

    filename = str(d / 'test_mat_database.pkl')

    test_material = Material(
        name='test',
        composition='test',
        density=0.,
        thermal_conductivity=0.,
    )

    test_material.save_to(filename)

    print(filename)

    assert os.path.exists(filename)
